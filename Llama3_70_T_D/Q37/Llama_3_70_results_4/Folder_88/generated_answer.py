def filter_chars(s):
    chars_to_remove = set(s[69:81]).intersection({chr(i) for i in range(ord('@'), ord('q'))})
    return ''.join((c for c in s if c not in chars_to_remove))