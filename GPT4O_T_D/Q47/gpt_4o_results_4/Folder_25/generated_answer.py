def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    base_range = s[26:85]
    filtered_range = ''.join((char for char in base_range if char.isalpha())).lower()
    result = set()
    for length in range(30, 47):
        for i in range(len(filtered_range) - length + 1):
            sub = filtered_range[i:i + length]
            if is_palindrome(sub):
                result.add(sub)
    return result