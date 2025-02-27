def filter_chars(s: str) -> str:
    char_range = ''.join((chr(i) for i in range(32, 61)))
    filtered = ''.join((c for c in s if c in char_range))
    filtered = filtered.replace('3' * ((ord('D') - ord('3')) // (51 - ord('3'))), '')
    return filtered