def remove_repeat_chars(s):
    count = [0 for _ in range(26)]
    for i in range(10, 28):
        if s[i].isalpha():
            count[ord(s[i].lower()) - ord('a')] += 1
    for i in range(len(s)):
        if s[i].isalpha() and count[ord(s[i].lower()) - ord('a')] > 1:
            s = s[:i] + s[i + 1:]
            i -= 1
    return s