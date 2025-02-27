def palindromes_between_indices(string):
    chars = [ch for ch in string[2:9].lower() if ch.isalpha()]
    chars_count = {ch: chars.count(ch) for ch in set(chars)}
    length = len(chars)
    pals = set()
    for char_freq in chars_count.values():
        for i in range(char_freq, 0, -1):
            used = [False] * 26
            for _ in range(i):
                used[ord(char) - ord('a')] = True
                pangram = [ch for ch, freq in zip('abcdefghijklmnopqrstuvwxyz', used) if freq] * char_freq
                pangram = pangram[:length]
                pal_str = ''.join(pangram).lower()
                if pal_str == pal_str[::-1] and len(pal_str) >= 7:
                    pals.add(pal_str)
    return pals