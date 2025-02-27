def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = s[63:71].lower()
    filtered_s = ''.join(filter(str.isalpha, s))
    result = set()
    for i in range(len(filtered_s)):
        for j in range(4, 6):
            if i + j <= len(filtered_s):
                substring = filtered_s[i:i + j]
                if is_palindrome(substring):
                    result.add(substring)
    return result