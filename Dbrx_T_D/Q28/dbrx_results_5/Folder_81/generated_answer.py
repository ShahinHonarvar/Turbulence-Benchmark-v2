def return_nth_smallest_ascii(s):
    sorted_ascii = sorted((ord(c) for c in s[:14]))[:14]
    return chr(sorted_ascii[13])