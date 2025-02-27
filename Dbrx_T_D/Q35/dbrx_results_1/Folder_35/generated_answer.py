def remove_repeat_chars(s):
    start_index = 77
    end_index = 84
    char_count = {}
    for i in range(start_index, end_index):
        if s[i] in char_count:
            char_count[s[i]] += 1
        else:
            char_count[s[i]] = 1
    for char, count in char_count.items():
        if count > 1:
            s = s[:start_index] + ''.join((c for c in s[start_index:end_index] if c != char)) + s[end_index:]
    return s