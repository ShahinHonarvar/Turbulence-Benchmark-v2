def return_n_greatest_chars(s):
    greatest_chars = sorted([char for char in s if ord(char) in set((ord(c) for c in s)) and ord(char) >= 128][:58])
    return greatest_chars