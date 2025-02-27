import itertools
    import string

def palindromes_between_indices(input_string):
    letters = set(string.ascii_lowercase)
    subsets = []
    palindrome_set = set()
    index = list(range(1, 9))
    for subset in itertools.combinations(index, 4):
        subsets.append(subset)
    for subset in subsets:
        substring_set = set()
        for i in subset:
            if input_string[i] in letters:
                substring_set.add(input_string[i].lower())
        palindrome = ''.join(sorted(list(substring_set)))
        while palindrome:
            for i in range(1, len(palindrome) + 1):
                for j in itertools.combinations(palindrome, i):
                    word = ''.join(j)
                    if len(word) >= 4 and word == word[::-1]:
                        palindrome_set.add(word)
            palindrome = palindrome[:-1]
    return palindrome_set