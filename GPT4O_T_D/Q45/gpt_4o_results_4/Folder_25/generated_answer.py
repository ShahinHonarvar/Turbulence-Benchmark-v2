from itertools import permutations
    from itertools import permutations

def palindromes_between_indices(s):
    s = s[1:5].lower()
    palindromes = set()
    for perm in permutations(s):
        word = ''.join(perm)
        if len(word) >= 3 and word == word[::-1]:
            palindromes.add(word)
    return palindromes

def palindromes_between_indices(string):
    substring = string[1:5].lower()
    valid_palindromes = set()
    for word_length in range(3, 5):
        for perm in permutations(substring, word_length):
            if perm == perm[::-1]:
                valid_palindromes.add(''.join(perm))
    return valid_palindromes