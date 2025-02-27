def palindromes_between_indices(string):
    substring = string[5:8]
    letters = set()
    for char in substring:
        if char.isalpha():
            letters.add(char.lower())
    if len(letters) < 2:
        return set()
    palindromes = set()
    for length in range(4, len(substring)):
        for i in range(len(substring) - length + 1):
            for palindrome in generate_palindromes(substring[i:i + length], letters):
                palindromes.add(palindrome)
    return palindromes

def generate_palindromes(substring, letters):
    if len(substring) == 1:
        return set()
    palindromes = set()
    for letter in letters:
        for i in range(len(substring)):
            if substring[i] == letter or substring[i] == '':
                new_substring = list(substring)
                new_substring[i] = letter
                new_substring = ''.join(new_substring)
                if is_palindrome(new_substring):
                    palindromes.add(new_substring)
    return palindromes

def is_palindrome(string):
    return string == string[::-1]