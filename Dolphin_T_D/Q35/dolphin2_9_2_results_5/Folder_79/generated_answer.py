def remove_repeat_chars(s):
    counts = {}
    for i in range(1, 7):
        if s[i] in counts:
            counts[s[i]] += 1
        else:
            counts[s[i]] = 1
    result = ''
    for chr in s:
        if chr not in counts or counts[chr] == 1:
            result += chr
    return result