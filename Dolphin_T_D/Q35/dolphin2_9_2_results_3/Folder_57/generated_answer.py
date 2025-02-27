def remove_repeat_chars(s):
    freq_count = [0] * 256
    for i in range(25, 80):
        if freq_count[ord(s[i])] == 1:
            s = s[:i] + s[i + 1:]
            i -= 1
        else:
            freq_count[ord(s[i])] += 1
    return s