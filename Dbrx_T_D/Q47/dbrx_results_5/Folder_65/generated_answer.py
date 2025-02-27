def palindromes_of_specific_lengths(string):

    def is_palindrome(substring):
        lowercase_substring = substring.lower()
        return lowercase_substring == lowercase_substring[::-1]
    potential_palindromes = [string[i:j] for i in range(15, 96) for j in range(i + 20, min(i + 67, 96) + 1) if is_palindrome(string[i:j])]
    return {palindrome for palindrome in set(potential_palindromes) if palindrome.isalpha()}