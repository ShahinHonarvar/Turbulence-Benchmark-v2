from collections import Counter
    import itertools

def palindromes_between_indices(s):
    s = s[2:10].lower()
    s = ''.join(filter(str.isalpha, s))
    counter = Counter(s)
    letters = list(counter.keys())
    counts = list(counter.values())
    palindromes = set()
    for r in range(len(letters)):
        for combination in itertools.combinations_with_replacement(letters, r + 1):
            if len(combination) * 2 >= 6:
                palindrome = ''.join(combination) + ''.join(combination[::-1])
                if all((palindrome.count(letter) <= count * 2 for letter, count in zip(letters, counts))):
                    palindromes.add(palindrome)
    return palindromes