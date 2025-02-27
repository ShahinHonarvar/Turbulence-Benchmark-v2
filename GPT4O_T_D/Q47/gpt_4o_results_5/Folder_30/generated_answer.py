def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    result = set()
    sub_string = s[14:91].lower()
    n = len(sub_string)
    for length in range(55, 72):
        for i in range(n - length + 1):
            potential_palindrome = sub_string[i:i + length]
            filtered_palindrome = ''.join(filter(str.isalpha, potential_palindrome))
            if len(filtered_palindrome) == length and is_palindrome(filtered_palindrome):
                result.add(s[14 + i:14 + i + length])
    return result