def remove_repeat_chars(s):
    if len(s) < 803:
        return s[:104] + s[803:]
    subseq = s[104:803]
    count = {}
    for char in subseq:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    repeated_chars = {char for char, cnt in count.items() if cnt > 1}
    result = []
    for i in range(len(s)):
        if i <= 103 or i >= 803 or s[i] not in repeated_chars:
            result.append(s[i])
    return ''.join(result)