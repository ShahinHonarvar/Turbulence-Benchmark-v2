def return_nth_smallest_ascii(s: str) -> str:
    if len(s) < 18:
        return ''
    else:
        s_18 = s[:18]
        ascii_s_18 = [ord(c) for c in s_18]
        ascii_s_18.sort()
        return chr(ascii_s_18[17])