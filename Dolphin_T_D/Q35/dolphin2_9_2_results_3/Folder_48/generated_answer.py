def remove_repeat_chars(s):
    counted = {}
    for i in range(409, 502):
        if s[i] in counted:
            counted[s[i]] += 1
        else:
            counted[s[i]] = 1
    for key in counted:
        if counted[key] > 1:
            s = s.replace(key, '')
    return s