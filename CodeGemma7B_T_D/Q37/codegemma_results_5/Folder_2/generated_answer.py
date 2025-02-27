def filter_chars(str):
    return ''.join([ch for ch in str if 477 <= str.index(ch) <= 984 and ch in range(ord(',') + 1, ord('V') + 2)])