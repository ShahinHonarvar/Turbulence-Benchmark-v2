def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = ''.join(filter(str.isalpha, s)).lower()
    potential_palindromes = s[200:301]
    palindromes = set()
    for length in range(10, 51):
        for start in range(len(potential_palindromes) - length + 1):
            substring = potential_palindromes[start:start + length]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes