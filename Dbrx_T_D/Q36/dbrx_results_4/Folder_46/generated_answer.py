def filter_chars(s: str) -> str:
    filtered_s = s[18:69][::-1]
    result = ''
    for char in filtered_s:
        if 'C' > char > '<':
            result += char
    return result[::-1] + s[:18] + s[69:]