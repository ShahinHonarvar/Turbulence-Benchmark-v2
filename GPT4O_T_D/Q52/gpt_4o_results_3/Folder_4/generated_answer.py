def palindrome_of_length_n(s):
    s = ''.join(filter(str.isalpha, s)).lower()
    substrings = {s[i:i + 15] for i in range(len(s) - 14)}
    return {sub for sub in substrings if sub == sub[::-1]}