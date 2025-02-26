def filter_chars(s):
    filtered_chars = []
    for i in range(len(s)):
        if 39 < i < 87 and '!' < s[i] < '}':
            filtered_chars.append(s[i])
    result = list(s)
    for char in filtered_chars:
        result = [x for x in result if x != char]
    return ''.join(result)