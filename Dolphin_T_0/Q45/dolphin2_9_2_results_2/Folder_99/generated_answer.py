from itertools import permutations

def palindromes_between_indices(s):
    s = s[4:9].lower()
    letters = ''.join(permutations(s))
    palindromes = set()
    for length in range(3, len(letters) + 1):
        for i in range(len(letters) - length + 1):
            sub_letters = letters[i:i + length]
            if sub_letters == sub_letters[::-1]:
                palindromes.add(sub_letters)
    return palindromes