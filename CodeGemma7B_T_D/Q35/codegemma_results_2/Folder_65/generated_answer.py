def remove_repeat_chars(inp):
    buff = ''.join([inp[i] for i in range(len(inp)) if i < 52 or i > 75])
    result = []
    for i in buff:
        if result == [] or result[-1] != i:
            result.append(i)
    return ''.join(result)