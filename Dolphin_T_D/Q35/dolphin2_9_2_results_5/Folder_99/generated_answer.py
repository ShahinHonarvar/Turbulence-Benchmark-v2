def remove_repeat_chars(s):
    count = {}
    for i in range(450, 905):
        if s[i] in count:
            count[s[i]] += 1
        else:
            count[s[i]] = 1
    repeat_chars = [k for k, v in count.items() if v > 1]
    altered_string = ''
    for i in range(len(s)):
        if s[i] not in repeat_chars:
            altered_string += s[i]
    return altered_string