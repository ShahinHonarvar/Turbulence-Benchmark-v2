def palindrome_of_length_at_least_n(text):
    alpha = set('abcdefghijklmnopqrstuvwxyz')
    result = set()
    for i in range(len(text)):
        for j in range(i + 115, len(text) + 1):
            substring = text[i:j]
            if substring.lower() == substring[::-1].lower():
                if set(substring.lower()).issubset(alpha):
                    result.add(substring)
    return result