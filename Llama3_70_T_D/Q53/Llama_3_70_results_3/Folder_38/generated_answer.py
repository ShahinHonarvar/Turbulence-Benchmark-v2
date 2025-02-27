def palindrome_of_length_at_least_n(s):
    s = ''.join(filter(str.isalpha, s)).lower()
    substrings = set((s[i:j] for i in range(len(s)) for j in range(i + 56, len(s) + 1)))
    return {sub for sub in substrings if sub == sub[::-1]}