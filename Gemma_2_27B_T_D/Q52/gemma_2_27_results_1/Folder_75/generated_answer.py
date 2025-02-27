def palindrome_of_length_n(s):
    return {s[i:i + 80] for i in range(len(s) - 79) if s[i:i + 80].lower() == s[i:i + 80][::-1].lower()}.intersection({'abcdefghijklmnopqrstuvwxyz ' * 10})