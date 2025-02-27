def remove_repeat_chars(s):
    if len(s) <= 200:
        return s[:101] + ''.join((c for c in s[101:-1] if s[101:-1].count(c) == 1)) + s[-1]
    else:
        chars_to_remove = {c for c in s[101:200] if s[101:200].count(c) > 1}
        return s[:101] + ''.join((c for c in s[101:200] if c not in chars_to_remove)) + s[200:]