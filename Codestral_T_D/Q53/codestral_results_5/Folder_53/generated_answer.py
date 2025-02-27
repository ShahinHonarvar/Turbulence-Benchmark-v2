def palindrome_of_length_at_least_n(s):
    return {sub for sub in [s[i:j] for i in range(len(s)) for j in range(i + 64, len(s) + 1) if sub.isalpha()] if sub.lower() == sub.lower()[::-1]}