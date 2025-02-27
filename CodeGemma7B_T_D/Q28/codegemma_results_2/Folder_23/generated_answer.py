def return_nth_smallest_ascii(s):
    answer = min(s[29:48], key=ord) if len(s) >= 48 else ''
    return answer