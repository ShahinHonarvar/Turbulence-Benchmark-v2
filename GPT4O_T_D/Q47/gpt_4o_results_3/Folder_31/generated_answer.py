def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    selected_substring = ''.join([ch for ch in s[11:84] if ch.isalpha()]).lower()
    palindromes = set()
    for length in range(37, 61):
        for i in range(len(selected_substring) - length + 1):
            substring = selected_substring[i:i + length]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes