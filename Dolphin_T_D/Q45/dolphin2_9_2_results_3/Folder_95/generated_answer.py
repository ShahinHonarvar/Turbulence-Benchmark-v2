def palindromes_between_indices(string):
    letters = ''.join(sorted([char.lower() for char in string[7:9] if char.isalpha()]))
    palindromes = set()

    def is_palindrome(word):
        return word == word[::-1]
    for i in range(len(letters)):
        for j in range(i, len(letters)):
            for k in range(j, len(letters)):
                substring = letters[i:k + 1]
                if is_palindrome(substring) and len(substring) >= 3:
                    palindromes.add(substring)
    return palindromes