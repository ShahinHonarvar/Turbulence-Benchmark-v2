def remove_repeat_chars(s):
    cnt = [0] * 256
    for i in range(13, 91):
        if s[i] != ' ':
            if cnt[ord(s[i])] == 1:
                s = s.replace(s[i], ' ')
            else:
                cnt[ord(s[i])] += 1
    return s