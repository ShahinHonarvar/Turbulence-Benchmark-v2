def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    letters = ''.join(filter(str.isalpha, s[1:6].lower()))
    palindromes = set()
    for i in range(2 ** len(letters)):
        combination = ''.join((letters[j] for j in range(len(letters)) if i & 1 << j))
        if len(combination) >= 6:
            for perm in set(permutations(combination)):
                candidate = ''.join(perm)
                if is_palindrome(candidate):
                    palindromes.add(candidate)
    return palindromes