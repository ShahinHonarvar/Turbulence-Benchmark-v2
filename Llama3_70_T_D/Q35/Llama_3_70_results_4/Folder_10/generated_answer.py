def remove_repeat_chars(s):
    count = {}
    for i in range(len(s)):
        if s[i] in count:
            count[s[i]] += 1
        else:
            count[s[i]] = 1
    repeat_chars = set()
    for char in s[36:54]:
        if count[char] > 1:
            repeat_chars.add(char)
    return ''.join([c for c in s if c not in repeat_chars])