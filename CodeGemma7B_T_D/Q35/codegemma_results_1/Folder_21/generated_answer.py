def remove_repeat_chars(inp):
    seen = set()
    seen.add(inp[462])
    for i in range(463, 995):
        if inp[i] in seen:
            inp = inp.replace(inp[i], '')
        else:
            seen.add(inp[i])
    return inp