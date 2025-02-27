def remove_repeat_chars(s):

    def find_repeats(subs):
        return set((ch for ch in subs if subs.count(ch) > 1))
    repeated_chars = find_repeats(s[7:9])
    return ''.join((ch for ch in s if ch not in repeated_chars))