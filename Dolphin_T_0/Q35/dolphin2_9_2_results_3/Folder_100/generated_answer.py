def remove_repeat_chars(s):
    diff = [0] * 128
    ans = ''
    for i in range(len(s)):
        if 44 < i < 78 and s[i] != ' ' and (diff[ord(s[i])] != 0):
            diff[ord(s[i])] += 1
        else:
            ans += s[i]
    return ans