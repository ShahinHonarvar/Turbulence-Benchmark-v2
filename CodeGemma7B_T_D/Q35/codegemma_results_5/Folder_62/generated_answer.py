def remove_repeat_chars(word):
    seen = set()
    res = []
    for letter in word:
        if letter not in seen and 50 <= len(res) <= 92:
            seen.add(letter)
            res.append(letter)
    return ''.join(res)