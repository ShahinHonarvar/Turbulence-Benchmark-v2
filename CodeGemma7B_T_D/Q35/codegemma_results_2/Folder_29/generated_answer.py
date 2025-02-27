def remove_repeat_chars(word):
    seen = {}
    output = []
    for i, letter in enumerate(word):
        if i < 70 or i > 98:
            continue
        if letter in seen:
            seen[letter] += 1
            if seen[letter] > 1:
                continue
        seen[letter] = 1
        output.append(letter)
    return ''.join(output)