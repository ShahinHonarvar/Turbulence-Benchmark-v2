def filter_chars(s):
    result = []
    for char in s:
        if 41 <= ord(char) <= 79 and 'f' <= char <= '|' or not 41 <= ord(char) <= 79:
            if not result or char != result[-1]:
                result.append(char)
        elif result and result[-1] == char:
            result.append(char)
    return ''.join(result)