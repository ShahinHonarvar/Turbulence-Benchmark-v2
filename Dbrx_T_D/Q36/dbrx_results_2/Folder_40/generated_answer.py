def filter_chars(s: str) -> str:
    alphabet = {chr(i): i for i in range(ord('A'), ord('Z') + 1)}
    alphabet.update({chr(i): i for i in range(ord('a'), ord('z') + 1)})
    alphabet.pop('-')
    alphabet.pop('L')
    filtered_chars = [c for c in s if alphabet.get(c, 0) > alphabet['-'] and alphabet.get(c, 0) < alphabet['L']]
    return ''.join(filtered_chars)