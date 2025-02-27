import itertools

def palindromes_between_indices(string):
    sub_string = string[4:10]
    sub_string = ''.join(filter(str.isalpha, sub_string))
    sub_string = sub_string.lower()
    palindromes = set()
    for i in range(4, len(sub_string) + 1):
        for j in itertools.permutations(sub_string, i):
            word = ''.join(j)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes