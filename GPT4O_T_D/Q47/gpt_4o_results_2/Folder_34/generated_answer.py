def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    filtered_string = ''.join((ch for ch in s[200:301] if ch.isalpha()))
    palindromes = set()
    for i in range(len(filtered_string)):
        for j in range(i + 10, min(i + 51, len(filtered_string) + 1)):
            substring = filtered_string[i:j]
            if is_palindrome(substring.lower()):
                palindromes.add(substring)
    return palindromes