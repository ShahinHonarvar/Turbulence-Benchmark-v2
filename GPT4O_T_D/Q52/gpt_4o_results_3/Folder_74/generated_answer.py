def palindrome_of_length_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    n = 96
    substrings = set()
    lower_s = ''.join(filter(str.isalpha, s)).lower()
    for i in range(len(lower_s) - n + 1):
        substring = lower_s[i:i + n]
        if is_palindrome(substring):
            substrings.add(substring)
    return substrings