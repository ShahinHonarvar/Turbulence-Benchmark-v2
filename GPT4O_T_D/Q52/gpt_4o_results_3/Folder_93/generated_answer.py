def palindrome_of_length_n(s):
    n = 45
    s = ''.join(filter(str.isalpha, s)).lower()
    result = set()
    for i in range(len(s) - n + 1):
        current_substring = s[i:i + n]
        if current_substring == current_substring[::-1]:
            result.add(current_substring)
    return result