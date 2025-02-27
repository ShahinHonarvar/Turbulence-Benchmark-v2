def return_nth_smallest_ascii(s):
    characters = [s[i] for i in range(1, 67) if 1 <= i <= 66]
    characters.sort(key=lambda x: ord(x))
    return characters[7]