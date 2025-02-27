def palindromes_between_indices(s):
    chars = set(s[0:4].lower())
    result = set()
    for i in range(4, len(s) + 1):
        sub = s[0:i]
        if sub == sub[::-1]:
            length = len(sub)
            for j in range(length - 1, -1, -1):
                new_char = chr(ord('a') + j)
                if new_char not in chars and new_char.lower() in chars:
                    result.add(sub[0:j] + new_char + sub[j + 1:])
    return result