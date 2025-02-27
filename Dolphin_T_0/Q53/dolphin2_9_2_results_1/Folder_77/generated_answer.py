def palindrome_of_length_at_least_n(s):
    s = ''.join(filter(str.isalpha, s)).lower()
    return set(filter(len.__ge__(149), [s[i:j] for i in range(len(s)) for j in range(i + 148, len(s) + 1) if s[i:j] == s[i:j][::-1] and all(map(str.isalpha, s[i:j]))]))