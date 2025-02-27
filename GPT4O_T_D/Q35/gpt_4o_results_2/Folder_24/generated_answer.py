def remove_repeat_chars(s):
    middle_section = s[14:91]
    freq = {}
    for char in middle_section:
        freq[char] = freq.get(char, 0) + 1
    to_remove = {char for char, count in freq.items() if count > 1}
    result = []
    for char in s:
        if char in to_remove and 14 <= s.index(char) < 91:
            continue
        result.append(char)
    return ''.join(result)